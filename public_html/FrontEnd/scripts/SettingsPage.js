import React, { Component } from 'react';
import logo from '../Images/logoTransport.png';
import './SettingsPage.css';

class Page extends Component {
  render() {
    return (
      <div className="Page">
        <header className="Page-header">
          <img src={logo} className="Page-logo" alt="logo" />
          <h1 className="Page-title">Welcome to React</h1>
        </header>
        <p className="Page-intro">
          To get started, edit <code>src/Page.js</code> and save to reload.
        </p>
	   <label id="roomNumer">Your Room Number</label>
	   <input type="text"></input>
      </div>
    );
  }
}
