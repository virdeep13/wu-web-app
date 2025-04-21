import React from "react";
import "../Tab4Content.css";
const Tab3Content = () => {
  return (
    <div className="tab3-container">
      <h1>Choose your Professor</h1>

      <div class="academics-grid">
        <div className="academics-card1">
          <button>Arts & Science</button>
          <div class="content">
            <a href="https://d3223bbf7ikyj9.cloudfront.net/">
              Computer Science
            </a>
            <a href=" ">Digital Media Informatics</a>
            <a href=" ">Communication Studies</a>
            <a href=" ">Communication Studies</a>
          </div>
        </div>

        <div className="academics-card2">
          <button>Health & Human Services</button>
          <div class="content">
            <b href="">Apple</b>
            <b href="">Orange</b>
            <b href="">Banana</b>
          </div>
        </div>

        <div className="academics-card3">
          <button>Business</button>
          <div class="content">
            <c href="">Apple</c>
            <c href="">Orange</c>
            <c href="">Banana</c>
          </div>
        </div>

        <div className="academics-card4">
          <button>Engineering</button>
          <div class="content">
            <d href="">Apple</d>
            <d href="">Orange</d>
            <d href="">Banana</d>
          </div>
        </div>

        <div className="academics-card5">
          <button>Nursing</button>
          <div class="content">
            <e href="">Apple</e>
            <e href="">Orange</e>
            <e href="">Banana</e>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Tab3Content;
