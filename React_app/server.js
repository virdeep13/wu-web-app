const express = require('express');
const scrapeEvents = require('./scrape_events.js');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());

// Root route to check if the server is running
app.get('/', (req, res) => {
  res.send('Server is running! Use /events to fetch event data.');
});

app.get('/events', async (req, res) => {
  try {
    const events = await scrapeEvents();
    res.json(events);
  } catch (error) {
    console.error('Error scraping events:', error);
    res.status(500).send('Error scraping events');
  }
});

app.use( (req, res) => {
  res.status(404).send("404 URL NOT FOUND");
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

  