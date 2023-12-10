import logo from './logo.svg';
import './App.css';
import { Routes, Route} from "react-router-dom";
import Home from './components/Home';
import Cypher from './components/Cypher';
import DeCypher from './components/DeCypher';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Home/>}>
          <Route path='/Cypher' element={ <Cypher/> } />
          <Route path='/DeCypher' element={ <DeCypher/> } />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
