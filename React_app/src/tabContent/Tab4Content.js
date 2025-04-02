import React from 'react';
import '../Tab4Content.css';
const Tab4Content = () => {
  return( 
  
    <div className="tab4-container">
    <h1>academics</h1>
    <div className="search-bar">
      <input type="text" placeholder="Search academics" />
      <button>Categories</button>
      <button>Options</button>
    </div>

    <div class="academics-grid">
    <div className="academics-card1">
        <button>Arts & Science</button>
        <div class = "content">
            <a href ="ComputerScience.html">Computer Science</a>
            <a href ="https://www.alsfamilyfarms.com/?srsltid=AfmBOoq7Cj4OUnAcMrMonDc4eWxTIZ4-c5-MtWEQr9w_4bNQ1cTEsLBN">Orange</a>
            <a href ="https://miamifruit.org/collections/banana-pre-orders?srsltid=AfmBOop4p0jLLTyGZ-5LWXCgEqKS2P6pq5tVWsH-uv2ZCseuknEh6_Uh">Banana</a>
        </div>
    </div>

      <div className="academics-card2">
      <button>Health & Human Services</button>
        <div class = "content">
            <b href ="">Apple</b>
            <b href ="">Orange</b>
            <b href ="">Banana</b>
        </div>
    </div>

      <div className="academics-card3">
      <button>Business</button>
        <div class = "content">
            <c href ="">Apple</c>
            <c href ="">Orange</c>
            <c href ="">Banana</c>
        </div>
    </div>


      <div className="academics-card4">
      <button>Engineering</button>
        <div class = "content">
            <d href ="">Apple</d>
            <d href ="">Orange</d>
            <d href ="">Banana</d>
        </div>
    </div>

      <div className="academics-card5">
      <button>Engineering</button>
        <div class = "content">
            <e href ="">Apple</e>
            <e href ="">Orange</e>
            <e href ="">Banana</e>
        </div>
    </div>
  </div>
</div>
  );
};
export default Tab4Content;