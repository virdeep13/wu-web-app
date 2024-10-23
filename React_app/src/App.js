import React from 'react';
import './App.css';
import './index.css';
import Tabs from './Tabs';
import Tab1Content from './tabContent/Tab1Content'; 
import Tab2Content from './tabContent/Tab2Content'; 
import Tab3Content from './tabContent/Tab3Content'; 
import screenshot from './images/Screenshot 2024-10-22 201804.png';



function App() {
  const tabsData = [
    { title: 'Tab 1', content: <Tab1Content /> },
    { title: 'Tab 2', content: <Tab2Content /> },
    { title: 'Tab 3', content: <Tab3Content /> },


  ];



  return (
    <div className="App">
      <h1>Widener Web App</h1>
      <img src={screenshot} alt="Description" className="top-left-image" />

      <Tabs tabs={tabsData} />
    </div>
  );
}

export default App;
