import React, { Component } from 'react';
import { Route, BrowserRouter as Router } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Home } from './components/Home';

export default class App extends Component {
  static displayName = App.name;

  render () {
    return (
      <Layout>
      <Router>
        <Route exact path='/' component={Home} />
        </Router>
      </Layout>

    );
  }
}
