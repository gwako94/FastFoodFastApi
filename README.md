# FastFoodFastApi
[![Build Status](https://travis-ci.org/gwako94/FastFoodFastApi.svg?branch=develop)](https://travis-ci.org/gwako94/FastFoodFastApi)
[![Coverage Status](https://coveralls.io/repos/github/gwako94/FastFoodFastApi/badge.svg?branch=develop)](https://coveralls.io/github/gwako94/FastFoodFastApi?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/3760e59fbf8a5ee9a086/maintainability)](https://codeclimate.com/github/gwako94/FastFoodFastApi/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1720c0bcd2874ac5a384e1b2e1ba471a)](https://www.codacy.com/app/gwako94/FastFoodFastApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gwako94/FastFoodFastApi&amp;utm_campaign=Badge_Grade)

A restful api to power fast-food-fast application.

<h1>Description</h1>
FastFoodFastApi is a restful api that powers a fast food fast application and helps manage
orders and menus. The application provide features for registering a user, login the user, place an order,
update an order and retrieve orders.

<h2>Getting Started!</h2>
<ul>
  <li><p>Have python3 installed:</p><pre><code>python --v
    >> Python 3.5.2</code></pre></li>
  <li><p>Clone the active-api repo and cd into it:</p><code>git clone --single-branch -b challenge-2-final  https://github.com/gwako94/FastFoodFastApi.git</code></pre>         </li>
  <li><p>Install virtualenv:</p><pre><code>pip install virtualenv</code></pre></li>
  <li><p>Create a virtual environment:</p><pre><code>virtualenv -p python3 venv</code></pre></li>
   <li><p>Activate the virtual environment:</p><pre><code>source venv/bin/activate</code></pre></li>
  <li><p>Install dependencies:</p><pre><code>pip install -r requirements.txt</code></pre></li>
  <li><p>Check that dependencies have been installed:</p><pre><code>pip freeze</code></pre></li>
   <li><p>Set environment variables:</p><pre><code>source .env</code></pre></li>

</ul>

<h2>Running the application</h2>
<p><pre><code>flask run</code></pre></p>
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
          <td>POST <code>/auth/register</code></td>
          <td>Register a user.</td>
      </tr>
      <tr>
          <td>POST <code>/auth/login</code></td>
          <td>Login a user.</td>
      </tr>
      <tr>
          <td>POST  <code>/api/v1/orders</code></td>
          <td>Post an order.</td>
      </tr>
      <tr>
          <td>GET <code>/api/v1/orders</code></td>
          <td>Fetch all orders.</td>
      </tr>
      <tr>
          <td>GET <code>/api/v1/orders/&lt;order_id&gt;</code></td>
          <td>Fetch a specific order.</td>
      </tr>
      <tr>
          <td>PUT <code>/api/v1/orders/&lt;order_id&gt;</code></td>
          <td>Update a specific order status</td>
      </tr>
  </tbody>
</table>
<h2>Screenshots</h2>

![get](https://user-images.githubusercontent.com/25703581/46033612-4caae480-c107-11e8-9d5c-b8ff68731e95.png)

![login](https://user-images.githubusercontent.com/25703581/46033613-4ddc1180-c107-11e8-9f31-06250c00fe8b.png)

![place_order](https://user-images.githubusercontent.com/25703581/46033614-4ddc1180-c107-11e8-848b-d4f52f126cd5.png)

![register](https://user-images.githubusercontent.com/25703581/46033618-4ddc1180-c107-11e8-8cfa-c191026debe4.png)

![update](https://user-images.githubusercontent.com/25703581/46033619-4e74a800-c107-11e8-9105-be04708e04d9.png)

<h2>Testing</h2>
<p>Run the tests: </p>
<pre><code> $ nosetests </code></pre>

<h2>Author</h2>
  <li><a href="https://github.com/gwako94">Galgallo Wako</a></li>
  
<h2>License</h2>
  <p>MIT License<p>


