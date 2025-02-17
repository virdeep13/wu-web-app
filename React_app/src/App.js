import React, { useState } from 'react';
import './App.css';
import './index.css';
import Tab1Content from './tabContent/Tab1Content'; 
import Tab2Content from './tabContent/Tab2Content'; 
import Tab3Content from './tabContent/Tab3Content'; 
import Tab4Content from './tabContent/Tab4Content'; 

// Get the theme dropdown
const themeSelect = document.getElementById('theme');

// Apply the selected theme
themeSelect.addEventListener('change', function () {
  const selectedTheme = themeSelect.value;
  document.body.className = selectedTheme; // Add the theme class to the body
});


function App() {
  // Step 1: Use React state to track the active tab
  const [activeTab, setActiveTab] = useState(0);

  const tabsData = [
<<<<<<< HEAD
    { title: 'Tab 1', content: <Tab1Content /> },
    { title: 'Tab 2', content: <Tab2Content /> },
    { title: 'Tab 3', content: <Tab3Content /> },
=======
    { title: 'News', content: <Tab1Content /> },
    { title: 'Events', content: <Tab2Content /> },
    { title: 'Organizations', content: <Tab3Content /> },
  ];

  // Step 2: Handle tab click to set active tab
  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  return (
    <div className="App">
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