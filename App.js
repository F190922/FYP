import React from "react"
import Header from "./components/common/header/Header"
import "./App.css"
import Homepages from "./components/home/Homepages"
import Footer from "./components/common/footer/Footer"
import SinglePage from "./components/singlePage/SinglePage"
import Term from "./components/common/Term and Conditions/Term"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"

const App = () => {
  return (
    <>
      <Router>
        <Header />
        <Switch>
          <Route exact path='/' component={Homepages} />
          
          <Route path='/singlepage/:id' exact component={SinglePage} />
          <Route path="/Term" component={Term} />
          <Footer/>

        </Switch>       
        
        
        
      </Router>
    </>
  )
}

export default App
