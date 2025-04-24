import React from "react";
import "../Academics.css";
const Professor = () => {
  return (
    <div className="Academics-container">
      <h1>Professor</h1>
      <div class="academics-grid">
        {/* First button */}
        <div className="academics-dropdown">
          <button class="dropbtn">Arts & Science</button>
          <div class="dropdown-one">
            <p class="dItem activedrp">
              Science
              <div class="dropdown-two">
                <a href="https://d3223bbf7ikyj9.cloudfront.net/" class="dItem">
                  Computer Science/Information Systems
                </a>
                <a href="#" class="dItem">
                  Digital Media Informatics
                </a>
                <a href="#" class="dItem">
                  Mathematics
                </a>
              </div>
            </p>

            <p class="dItem activedrp">
              Social Science
              <div class="dropdown-two">
                <a href="#" class="dItem">
                  Political Science
                </a>
                <a href="#" class="dItem">
                  Psychology
                </a>
                <a href="#" class="dItem">
                  Criminal Justice
                </a>
              </div>
            </p>
            <p class="dItem activedrp">
              Humanities
              <div class="dropdown-two">
                <a href="#" class="dItem">
                  History
                </a>
                <a href="#" class="dItem">
                  Philosophy
                </a>
                <a href="#" class="dItem">
                  communications
                </a>
              </div>
            </p>
          </div>
        </div>

        {/* Second button */}
        <div class="academics-dropdown">
          <button class="dropbtn">Health & Human Services</button>
          <div class="dropdown-one">
            <p class="dItem activedrp">Secondary Education</p>
            <a class="dItem activedrp">Social work</a>
          </div>
        </div>

        {/* Third button */}
        <div className="academics-dropdown">
          <button class="dropbtn">Business</button>
          <div class="dropdown-one">
            <p class="dItem">Accounting</p>
            <a class="dItem">Business Analytics</a>
            <a class="dItem">Finance</a>
            <a class="dItem">Marketing</a>
          </div>
        </div>

        {/* Fourth button */}
        <div className="academics-dropdown">
          <button class="dropbtn">Engineering</button>
          <div class="dropdown-one">
            <p class="dItem">Robotics Engineering</p>
            <a class="dItem">Civil Engineering</a>
            <a class="dItem">Biomedical Engineering</a>
            <a class="dItem">International Engineering</a>
          </div>
        </div>

        {/* Fifth button */}
        <div className="academics-dropdown">
          <button class="dropbtn">Nursing</button>
        </div>
      </div>
    </div>
  );
};
export default Professor;
