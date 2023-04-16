import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './index.css'
import reportWebVitals from './reportWebVitals'

// component imports
import App from './Components/App/App'
import Home from './Components/Home/Home'
import Wanikani from './Components/Wanikani/Wanikani'
import WanikaniReviews from './Components/Wanikani/WanikaniReviews'

// bootstrap includes
import 'https://cdn.jsdelivr.net/npm/react/umd/react.production.min.js'
import 'https://cdn.jsdelivr.net/npm/react-dom/umd/react-dom.production.min.js'
import 'https://cdn.jsdelivr.net/npm/react-bootstrap@next/dist/react-bootstrap.min.js'
import 'bootstrap/dist/css/bootstrap.min.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <div style={{backgroundColor: 'rgb(255, 244, 227)'}}>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/wanikani/reviews' element={<WanikaniReviews />} />
          <Route path='/wanikani' element={<Wanikani />} />
          <Route path='/test' element={<App />} />
        </Routes>
      </BrowserRouter>
    </div>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals(); // @TODO see about setting up endpoint to monitor this?
