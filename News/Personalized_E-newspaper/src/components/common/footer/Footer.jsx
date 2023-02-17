import React from "react"
import "./footer.css"

const Footer = () => {
  return (
    <>
      <footer>
        <div className='container'>
          <div className='box logo'>
           <h3 className="Contact_us"><b>Contact us</b></h3>        
          </div>          
          <div className='box logo'>
           <h3 className="awais">Awais</h3>
            <p>Full Stack Developer.</p>
            <i className='fa fa-envelope'></i>
            <span> awaisabid100@gmail.com </span> <br /> 
          </div>
          <div className='box logo'>  
           <h3 className="mehrunisa">Mehr un nisa</h3>
            <p>Full Stack Developer.</p>
            <i className='fa fa-envelope'></i>
            <span> Mehr100@gmail.com </span>   
          </div>
          <div className='box logo'>
           <h3 className="anas">Anas</h3>
            <p>Full Stack Developer.</p>
            <i className='fa fa-envelope'></i>
            <span> Anas100@gmail.com </span> <br />
          </div>
        </div>
      </footer>
      <div className='legal'>
        <div className='container flexSB'>
          <p className="allrightsreserved">© All rights reserved</p>
        </div>
      </div>
    </>
  )
}

export default Footer
