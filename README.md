# FastFoodFastApi v2
[![Build Status](https://travis-ci.org/gwako94/FastFoodFastApi.svg?branch=develop)](https://travis-ci.org/gwako94/FastFoodFastApi)
[![Coverage Status](https://coveralls.io/repos/github/gwako94/FastFoodFastApi/badge.svg?branch=develop)](https://coveralls.io/github/gwako94/FastFoodFastApi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/3760e59fbf8a5ee9a086/maintainability)](https://codeclimate.com/github/gwako94/FastFoodFastApi/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1720c0bcd2874ac5a384e1b2e1ba471a)](https://www.codacy.com/app/gwako94/FastFoodFastApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gwako94/FastFoodFastApi&amp;utm_campaign=Badge_Grade)

A restful api to power fast-food-fast application.

<h1>Description</h1>
FastFoodFastApi is a restful api that powers a fast food fast application and helps manage
orders and menus. The application provide features for registering a user, logging in the user, adding and gettin menu place an order,update an order and retrieve users order history.

<h2>Development Setup</h2>
<ul>
  <li><p>Have python3 installed:</p><pre><code>python --v
    >> Python 3.5.2</code></pre></li>
  <li><p>Install virtualenv:</p><pre><code>pip install virtualenv</code></pre></li>
  <li><p>Clone the active-api repo and cd into it:</p><code>https://github.com/gwako94/FastFoodFastApi.git</code></pre></li>
  <li><p>Install dependencies:</p><code>pip install -r requirements.txt</code></pre></li>
  <li><p>Activate a virtual environment:</p><code>source env_name/bin/activate</code></pre></li>
  <li><p>Deactivate the virtual environment oncedone:</p><code>deactivate</code></pre></li>
</ul>

<h2>Running the application</h2><pre>
<code>python3 run.py</code>
</pre>
<p>Fire up postman and tests all the endpoints below:</p>
<table>
  <thead>
      <tr>
          <th><strong>API Endpoints</strong></th>
          <th><strong>Function</strong></th>
      </tr>
    </thead>
  <tbody>
      <tr>
          <td>POST <code>/api/v2/auth/register</code></td>
          <td>Register a user.</td>
      </tr>
      <tr>
          <td>POST <code>/api/v2/auth/login</code></td>
          <td>Login a user.</td>
      </tr>
      <tr>
          <td>PUT <code>/api/v2/users/&lt;user_id_id&gt;</code></td>
          <td>Promote a user to an admin</td>
      </tr>
          <tr>
          <td>POST <code>/api/v2/menu</code></td>
          <td>Post a menu</td>
      </tr>
          </tr>
          <tr>
          <td>GET <code>/api/v2/menu</code></td>
          <td>Post a menu</td>
      </tr>
      <tr>
          <td>POST  <code>/api/v2/users/orders</code></td>
          <td>GET all menu.</td>
      </tr>
      <tr>
          <td>GET <code>/api/v2/users/orders</code></td>
          <td>Fetch order history</td>
      </tr>
      <tr>
          <td>GET <code>/api/v2/orders</code></td>
          <td>Get all orders</td>
      </tr>
      <tr>
          <td>GET <code>/api/v2/orders/&lt;order_id&gt;</code></td>
          <td>Fetch a specific order.</td>
      </tr>
      <tr>
          <td>PUT <code>/api/v2/orders/&lt;order_id&gt;</code></td>
          <td>Update a specific order status</td>
      </tr>
  </tbody>
</table>
<h2>Screenshots</h2>

![v2_register](https://user-images.githubusercontent.com/25703581/46500602-e2dbba80-c82b-11e8-99d0-bfb045a0f063.png)

![place](https://user-images.githubusercontent.com/25703581/46500598-e2432400-c82b-11e8-9db3-869f6ac9388b.png)

![update](https://user-images.githubusercontent.com/25703581/46500600-e2dbba80-c82b-11e8-8d75-291c3354dcf4.png)

<h2>Testing</h2>
<p>Run the tests: </p>
<pre><code> $ nosetests </code></pre>

<h2>Hosting</h2>
<li><a href="https://herokufastfoodapi.herokuapp.com/">Heroku</a></li>

<h2>Author</h2>
  <li><a href="https://github.com/gwako94">Galgallo Wako</a></li>
  
<h2>License</h2>
  <p>MIT License<p>


