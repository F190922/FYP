import React from "react"
import Header from "./components/common/header/Header"
import "./App.css"
import Homepages from "./components/home/Homepages"
import Footer from "./components/common/footer/Footer"
import SinglePage from "./components/singlePage/SinglePage"
import Term from "./components/common/Term and Conditions/Term"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import Login from "./components/common/login/Login"
import Register from "./components/common/Register/Register"
import Cards from "./components/common/Cards/Cards"

const App = () => {
  return (
    <>
      <Router>

      
      
      <Header />
      <Route  path='/login'  component={Login} />
        <Route  path='/register'  component={Register} />
        <Switch>
        
        
        
        <Route  path='/' exact component={Homepages} />
        
          <Route path='/singlepage/:id' exact component={SinglePage} />
          <Route path="/Term" component={Term} />
          <Footer/>

        </Switch>       
        
        
        
      </Router>
    </>
  )
}

export default App
