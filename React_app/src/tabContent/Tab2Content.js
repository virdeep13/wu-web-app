import React from 'react';
import Tabs from '../Tabs';

const Tab2Content = () => {
  const nestedTabsData = [
  { title: 'Nested Tab 1', content: <div>Content for Nested Tab 1</div> },
  { title: 'Nested Tab 2', content: <div>Content for Nested Tab 2</div> },
  ];

  return( 
  <div>
  <h2>Events and announcements </h2>
  <Tabs tabs={nestedTabsData} />
</div>
  );
  
  
};

export default Tab2Content;
