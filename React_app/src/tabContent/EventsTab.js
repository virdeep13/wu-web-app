import React, { useEffect, useState } from "react";

function EventsTab() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchEvents() {
      try {
        const response = await fetch("http://localhost:3000/events");
        const data = await response.json();
        console.log("Fetched events:", data); // Add this line
        setEvents(data);
      } catch (error) {
        console.error("Error fetching events:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchEvents();
  }, []);

  if (loading) return <p>Loading events...</p>;

  return (
    <div>
      <h1>Upcoming Events</h1>
      <ul>
        {events.map((event, index) => (
          <li key={index}>
            <h2>{event.details}</h2>
            <p>
              <strong>Date:</strong> {event.date}
            </p>
            <p>
              <strong>Open To:</strong> {event.open_to}
            </p>
            <p>
              <strong>Description:</strong> {event.description}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default EventsTab;
