<!DOCTYPE html>
2	<html>
3	  <head>
4	    <meta name="viewport" content="width=device-width, initial-scale=1">
5	  </head>
6	  <body>
7	    <!-- Replace "test" with your own sandbox Business account app client ID -->
8	    <script src="https://www.paypal.com/sdk/js?client-id=test&currency=USD"></script>
9	    <!-- Set up a container element for the button -->
10	    <div id="paypal-button-container"></div>
11	    <script>
12	      paypal.Buttons({
13	        // Sets up the transaction when a payment button is clicked
14	        createOrder: (data, actions) => {
15	          return actions.order.create({
16	            purchase_units: [{
17	              amount: {
18	                value: '77.44' // Can also reference a variable or function
19	              }
20	            }]
21	          });
22	        },
23	        // Finalize the transaction after payer approval
24	        onApprove: (data, actions) => {
25	          return actions.order.capture().then(function(orderData) {
26	            // Successful capture! For dev/demo purposes:
27	            console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
28	            const transaction = orderData.purchase_units[0].payments.captures[0];
29	            alert(`Transaction ${transaction.status}: ${transaction.id}\n\nSee console for all available details`);
30	            // When ready to go live, remove the alert and show a success message within this page. For example:
31	            // const element = document.getElementById('paypal-button-container');
32	            // element.innerHTML = '<h3>Thank you for your payment!</h3>';
33	            // Or go to another URL:  actions.redirect('thank_you.html');
34	          });
35	        }
36	      }).render('#paypal-button-container');
37	    </script>
38	  </body>
39	</html>