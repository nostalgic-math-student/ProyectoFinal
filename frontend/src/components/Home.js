import React from 'react'
import { Outlet } from 'react-router-dom';

const Home = () => {
  return (
    <div>

    <div className="hero bg-base-200">
        <div className='hero-content mx-auto flex-col text-center columns-2'>      
        <div className=' w-full'>
    <h1>
        S4: Shahir 
    </h1>
        </div>
        </div>
    </div>
    <div >
        <Outlet/>
    </div>
    </div>
  )
}

export default Home