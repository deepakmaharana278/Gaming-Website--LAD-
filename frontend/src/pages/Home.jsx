import React from 'react'
import Layout from '../components/Layout'
import HomeSlider from './HomeSlider'

const Home = () => {
  return (
      <Layout>
          <div>
        <HomeSlider />
        <div className='mt-12'>
          welcome 
        </div>
          </div>
    </Layout>
  )
}

export default Home