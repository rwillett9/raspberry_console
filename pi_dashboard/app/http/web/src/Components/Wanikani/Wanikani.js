import React, { Component } from 'react'
import axios from 'axios'


class Home extends Component {

  constructor(props) {
    super(props)
    this.state = {
      is_loading: true,
      username: ''
    }
  }

  // this is called after render
  componentDidMount() {
    axios.get('http://localhost:4433/test')
      .then(res => {
        console.log(this.state)
        this.setState({ is_loading: false, username: res.data.username })
      })
      .catch(err => {
        console.error('Error: ', err.message)
      })
  }

  render() {
    return (
      <div>
        <div>WANIKANI SCREEN</div>
        <div>{this.state.username}</div>
      </div>
    )
  }
}

export default Home
