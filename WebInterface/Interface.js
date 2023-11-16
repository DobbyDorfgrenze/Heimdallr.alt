

window.addEventListener("load", (event) => {
    

    document.getElementById("networkButton").addEventListener("click", async () => {
        console.log("dsjkbhdsjkbajkbd");
        
        const data = document.getElementById("networkInput");
        const encodedMessage = new TextEncoder().encode(data);
        console.log(encodedMessage)
        const ws = new WebSocket("ws://localhost:9999");
        ws.send(encodedMessage);
    });
});
// JavaScript for displaying dynamic content (replace with actual data)
document.addEventListener('DOMContentLoaded', ()=>  {
    const statisticsWidget = document.querySelector('.widget#statistics .widget-content');
    const chartWidget = document.querySelector('.widget#vulnerability-distribution .widget-content');

    // Simulated data (replace with real data)
    const statisticsData = {
        activeScans: 5,
        detectedVulnerabilities: 132,
    };

    const chartData = {
        // Replace with data for your chart library (e.g., Chart.js, D3.js)
    };

    // Update content with dynamic data
    statisticsWidget.innerHTML = `
        <p>Active Scans: ${statisticsData.activeScans}</p>
        <p>Detected Vulnerabilities: ${statisticsData.detectedVulnerabilities}</p>
    `;

    // Update chart content (use your preferred chart library)
    // Example: createChart(chartWidget, chartData);


});


/*const socket = new WebSocket("ws://localhost:5876");

// Handle messages from the server
socket.addEventListener("message", (event) => {
    const messageFromServer = event.data;
    console.log(`Received from server: ${messageFromServer}`);
    
    // Update your web page with the received data
    // For example, you can add it to a div element
    const resultDiv = document.getElementById("result");
    resultDiv.textContent = messageFromServer;
});

// Handle connection errors
socket.addEventListener("error", (event) => {
    console.error("WebSocket error:", event);
});*/
