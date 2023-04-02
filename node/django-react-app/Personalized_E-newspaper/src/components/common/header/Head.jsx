import React from "react"
import { useAuth0 } from "@auth0/auth0-react";
import { useHistory } from "react-router-dom";
import Login from "../login/Login";
const Head = () => {
  const history = useHistory();
  const { loginWithRedirect,user, isAuthenticated, isLoading } = useAuth0();
  const { logout } = useAuth0();
  return (
    <>
      <section className='head'>
        <div className='container flexSB paddingTB'>
          <div className='logo'>
         
          <h1>𝕰-𝕹𝖊𝖜𝖘𝖕𝖆𝖕𝖊𝖗</h1>
            
          </div>
           <div className='ad'>
           { 
                isAuthenticated ?( <h3>
                <h3 onClick={()=>{ logout({returnTo: window.location.origin})
         
         }}>
                𝒍𝒐𝒈𝒐𝒖𝒕
      </h3>
                </h3>
             ):(
             <h3>
              <h3 onClick={()=>{
         loginWithRedirect()
         }}>𝑳𝒐𝒈𝒊𝒏</h3>
              </h3>
             )}
          </div>
        </div>
      </section>
    </>
  )
}
export default Head
