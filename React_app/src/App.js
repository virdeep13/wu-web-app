import React, { useState } from "react";
import "./App.css";
import "./index.css";
import "./styles.css";
import EventsTab from "./tabContent/EventsTab";
import Professor from "./tabContent/Professor";
import Academics from "./tabContent/Academics";

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
    { title: "Academics", content: <Academics /> },
    { title: "Events", content: <EventsTab /> },
    { title: "Choose your Professor", content: <Professor /> },
  ];

  // Step 2: Handle tab click to set active tab
  const handleTabClick = (index) => {
    setActiveTab(index);
  }; 

return (
 
  <div className="App">

    <h1>Widener Web App</h1>

    



    {/* Step 3: Render Tabs */}

      <div className="tabs">
        {tabsData.map((tab, index) => (
          <button
            key={index}
            className={`tab-button ${activeTab === index ? "active" : ""}`}
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