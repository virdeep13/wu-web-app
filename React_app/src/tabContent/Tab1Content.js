import React from 'react';
import Tabs from '../Tabs'; 
import NestedTab1Content from './NestedTab1'; 


const Tab1Content = () => {
  
  const nestedTabsData = [
    { title: 'Nested Tab 1', content: <NestedTab1Content/> },
    { title: 'Nested Tab 2', content: <div>Content for Nested Tab 2</div> },
  ];

  return (
    <div>
      <h2>News Updates</h2>
      <Tabs tabs={nestedTabsData} /> 
    </div>
  );
};

export default Tab1Content;
