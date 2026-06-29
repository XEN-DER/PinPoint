import { Server } from 'socket.io';
import fs from 'fs';

const dataFile = './data.json';

// Pre-seeded data if none exists
const preseededIssues = [
  {
    id: "ISU-2024-001",
    title: "Pothole on Main St",
    category: "Infrastructure",
    severity: "Medium",
    status: "Open",
    locality: "Downtown",
    lat: 34.0522,
    lng: -118.2437,
    date: new Date().toISOString(),
    reporter: "John Doe",
    upvotes: 5,
    downvotes: 0,
    disputed: false,
    description: "Large pothole in the right lane."
  }
];

function initData() {
  if (!fs.existsSync(dataFile)) {
    fs.writeFileSync(dataFile, JSON.stringify(preseededIssues, null, 2));
  }
}

export function socketIoPlugin() {
  return {
    name: 'vite-plugin-socket-io',
    configureServer(server) {
      initData();
      const io = new Server(server.httpServer, {
        cors: { origin: '*' }
      });

      io.on('connection', (socket) => {
        // Send initial data to the newly connected client
        try {
          const data = JSON.parse(fs.readFileSync(dataFile, 'utf-8'));
          socket.emit('init_issues', data);
        } catch(e) {
          console.error("Failed to read init data", e);
        }

        socket.on('sync_issues', (issues) => {
           try {
             fs.writeFileSync(dataFile, JSON.stringify(issues, null, 2));
             // Broadcast to all other clients to sync them up
             socket.broadcast.emit('init_issues', issues);
           } catch(e) {
             console.error("Error syncing issues", e);
           }
        });

        socket.on('add_issue', (issue) => {
           try {
             const data = JSON.parse(fs.readFileSync(dataFile, 'utf-8'));
             data.push(issue);
             fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));
             io.emit('issue_added', issue);
           } catch(e) {
             console.error("Error adding issue", e);
           }
        });

        socket.on('update_issue', (updatedIssue) => {
           try {
             const data = JSON.parse(fs.readFileSync(dataFile, 'utf-8'));
             const index = data.findIndex(i => i.id === updatedIssue.id);
             if (index !== -1) {
               data[index] = updatedIssue;
               fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));
               io.emit('issue_updated', updatedIssue);
             }
           } catch(e) {
             console.error("Error updating issue", e);
           }
        });
      });
    }
  };
}
