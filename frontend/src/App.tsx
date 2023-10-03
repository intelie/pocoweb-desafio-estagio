import { styled } from "styled-components";

import Challenge from "./components/Challenge";

const Container = styled.div`
  width: 100vw;
`;

const Title = styled.h1`
  text-align: center;
`;

function App() {
  return (
    <Container>
      <Title>Desafio estágio</Title>
      <Challenge />
    </Container>
  );
}

export default App;
