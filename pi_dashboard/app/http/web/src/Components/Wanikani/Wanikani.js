import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'



function Wanikani() {
  const [isLoading, setLoading] = useState(true)
  const [username, setUsername] = useState('')

  useEffect(() => {
    axios.get('http://localhost:4433/test')
      .then(res => {
        // update state vars
        setUsername(res.data.username)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error: ', err.message)
      })
  })

  return (
    <Container className='m-3'>
      <Row className='justify-content-start my-2'>
        <Col md='auto'>
          <Button href='/'>Back</Button>
        </Col>
        <Col className='' lg={true}>
          username: {username}
        </Col>
        <Col md='auto'>
          <img style={{ width: 200, height: 200}} src={require('../Images/crabigator.webp')} alt='Wanikani Dashboard' />
        </Col>
      </Row>
      <Row className='justify-content-md-center my-2'>

      </Row>
      <Row className='my-2'>

      </Row>
      <Button href='/wanikani/reviews'>Recent Reviews</Button>
    </Container>
  )
}

export default Wanikani
