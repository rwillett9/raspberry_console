import React, { useState, useEffect } from 'react'
import axios from 'axios'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'


function WanikaniReviews() {
  const [isLoading, setLoading] = useState(true)
  const [reviews, setReviews] = useState(true)
  const [kanji, setKanji] = useState(true)

  useEffect(() => {
    axios.get('http://localhost:4433/recent-reviews')
      .then(res => {
        // update state vars
        setReviews(res.data.reviews)
        setKanji(res.data.subjects)
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
          <Button href='/wanikani'>Back</Button>
        </Col>
      </Row>
      <div>REVIEWS SCREEN</div>
    </Container>
  )
}

export default WanikaniReviews
