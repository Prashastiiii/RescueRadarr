import React from 'react';
import './Education.css';

const Education = () => {
  return (
    <div className="education">
      <h2>Educational Resources</h2>
      <div className="resources">
        <div className="videos">
          <h3>Videos</h3>
          <ul>
            <li>
              <iframe
                width="420"
                height="315"
                src="https://www.youtube.com/embed/BaWnRznp1AU"
                title="YouTube video player"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            </li>
            <li>
              <iframe
                width="420"
                height="315"
                src="https://www.youtube.com/embed/BLEPakj1YTY"
                title="YouTube video player"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            </li>
            <li>
              <iframe
                width="420"
                height="315"
                src="https://www.youtube.com/embed/KwAKjtkpdP4"
                title="YouTube video player"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            </li>
          </ul>
        </div>
        <div className="articles">
          <h3>Articles</h3>
          <ul>
            <li>
              <iframe
                width="100%"
                height="400px"
                src="https://journalajgr.com/index.php/AJGR/article/view/217"
                title="Disaster Management Essay"
                frameBorder="0"
                allowFullScreen
              ></iframe>
            </li>
            <li>
              <iframe
                width="100%"
                height="400px"
                src="https://unacademy.com/content/nda/study-material/geography/preventive-measures-for-earthquake/"
                title="Disaster Management Essay"
                frameBorder="0"
                allowFullScreen
              ></iframe>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Education;
