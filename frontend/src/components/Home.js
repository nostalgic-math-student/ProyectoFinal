import React from 'react';
import { Outlet, Link } from 'react-router-dom'; // Importa Outlet y Link de react-router-dom para la navegación.

const Home = () => {
  return (
    <div>
      <div className="hero bg-base-200">
        <div className='hero-content mx-auto flex-col text-center columns-3'>      
          <div className='w-full columns-3'>
            {/* Link a la página de cifrado */}
            <Link to='/Cypher'>
              <div className='btn btn-primary'>Go to Encrypt</div>
            </Link>
            <p className='py-3 text-xl font-bold'>
              S4: Shamir Secret Sharing Scheme
            </p>
            {/* Link a la página de descifrado */}
            <Link to='/DeCypher'>
              <div className='btn btn-primary'>Go to Decrypt</div>
            </Link>
          </div>
        </div>
      </div>
      {/* Outlet para renderizar los componentes hijos en la ruta actual */}
      <div>
        <Outlet/>
      </div>
    </div>
  )
}

export default Home