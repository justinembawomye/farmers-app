import React, { Component } from 'react'

export class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-sm navbar-light bg-light">
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
          <a className="navbar-brand" href="#">Pride Farm</a>
          <a className="nav-item right" href="#">Home</a>
          <a className="nav-item right ml-2" href="#">About</a>
        </div>
      </nav>
    )
  }
}

export default Header