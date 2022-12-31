import React, { Component } from 'react'

class Home extends Component {

  // constructor(props) {
  //   super(props)
  // }

  render() {
    return (
      <div>
        <a href='/wanikani'><img src={require('./crabigator.webp')} alt='Wanikani' /></a>
      </div>
    )
  }
}

export default Home
