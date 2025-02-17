import React from 'react';
import '../Tab4Content.css';
const Tab4Content = () => {
  return( 
  
    <div className="tab4-container">
    <h1>Organizations</h1>
    <div className="search-bar">
      <input type="text" placeholder="Search Organizations" />
      <button>Categories</button>
      <button>Options</button>
    </div>

    <div class="organization-grid">
    <div className="organization-card1"> Arts & Sciences
        <button>Computer Science</button>
        <div class = "content">
            <a href ="">Apple</a>
            <a href ="">Orange</a>
            <a href ="">Banana</a>
        </div>
    </div>

      <div className="organization-card2">Health & Human Services</div>
      <div className="organization-card3">Business</div>
      <div className="organization-card4">Engineering</div>
      <div className="organization-card5">Nursing</div>
  </div>
</div>
  );
};
export default Tab4Content;