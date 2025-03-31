import React, { useState } from 'react';
import './App.css';
import './index.css';
import Tabs from './Tabs';
import Tab1Content from './tabContent/Tab1Content'; 
import EventsTab  from './tabContent/EventsTab'; 
import Tab3Content from './tabContent/Tab3Content'; 
import screenshot from './images/Screenshot 2024-10-22 201804.png';

function App() {
  // Step 1: Use React state to track the active tab
  const [activeTab, setActiveTab] = useState(0);

  const tabsData = [
    { title: 'News', content: <Tab1Content /> },
    { title: 'Events', content: <EventsTab /> },
    { title: 'Organizations', content: <Tab3Content /> },
  ];

  // Step 2: Handle tab click to set active tab
  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  return (
    <div className="App">
      <h1>Widener Web App</h1>
      <img src={screenshot} alt="Description" className="top-left-image" />

      {/* Step 3: Render Tabs */}
      <div className="tabs">
        {tabsData.map((tab, index) => (
          <button
            key={index}
            className={`tab-button ${activeTab === index ? 'active' : ''}`}
            onClick={() => handleTabClick(index)}
            data-tab-target={`#${index}`}
          >
            {tab.title}
          </button>
        ))}
      </div>

      {/* Step 4: Render active tab content */}
      <div className="tab-content">
        {tabsData.map((tab, index) => (
          <div
            key={index}
            className={`tab-panel ${activeTab === index ? 'active' : ''}`}
            data-tab-content
          >
            {activeTab === index && tab.content}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
