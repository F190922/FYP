import React, { useState } from "react"
import Head from "./Head"
import "./header.css"
import { Link } from "react-router-dom"


const Header = () => {
  const [navbar, setNavbar] = useState(false)
  
  return (
    <>
    
      <Head />
     
      <header>
        <div className='container paddingSmall'>
          <nav>
            <ul className={navbar ? "navbar" : "flex"} >
            
              <li>
                <Link to='/'>Home</Link>
              </li>
              
              <li>
                <Link to='/contact us'>Contact us</Link>
              </li>
              <li>
                <Link to='/Term'> Term and Conditions</Link>
              </li>
              
              <li><div class="dropdown">
              <button class="dropbtn">Select City</button>
              <div class="dropdown-content">
              <a href="#">Faisalabad</a>
              <a href="#">Lahore</a>
              <a href="#">Karachi</a>
              <a href="#">Islamabad</a>
              <a href="#">Multan</a>
              <a href="#">Chiniot</a>
              <a href="#">Okara</a>
             </div>
             </div></li>
             <div class="dropdown">
              <button class="dropbtn">Select Interest</button>
              <div class="dropdown-content">
              <a href="#">Fashion</a>
              <a href="#">Education</a>
              <a href="#">Sports</a>
              <a href="#">Comedy</a>
              
             </div>
             </div>
             
             <li><div className="textarea">
                <textarea id="textarea" name="w3review" rows="2" cols="50" placeholder="Searching News" ></textarea></div>
              </li>
            </ul>
            
           {/* <button className='barIcon' onClick={() => setNavbar(!navbar)}>
              {navbar ? <i className='fa fa-times'></i> : <i className='fa fa-bars'></i>}
            </button>*/}
        
          </nav>
          
        </div>
      </header>
      
    </>
  )
}

export default Header
