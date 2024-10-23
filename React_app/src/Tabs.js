import React, { useState } from 'react';

const Tabs = ({ tabs }) => {
  const [activeTab, setActiveTab] = useState(0);


  return (
    <div className="tabs">
      <ul className="tab-titles" role="tablist">
        {tabs.map((tab, index) => (
          <li
            key={index}
            role="tab"
            tabIndex={0}
            className={activeTab === index ? 'active' : ''}
            onClick={() => setActiveTab(index)}
            onKeyDown={(e) => e.key === 'Enter' && setActiveTab(index)}
            aria-selected={activeTab === index}
            aria-controls={`tab-content-${index}`}
          >
            {tab.title}
          </li>
        ))}
      </ul>
      <div className="tab-content" role="tabpanel" id={`tab-content-${activeTab}`}>
        {tabs[activeTab].content}
      </div>
    </div>
  );
};

export default Tabs;
