**Application Load Balancer (ALB)** for web traffic (HTTP/HTTPS).

### 🏛️ Key Steps for Setting Up an AWS Load Balancer

1.  **Create a Target Group:**
    * This is the group of resources (like **EC2 instances**) that will receive the traffic.
    * In the EC2 console, go to **Target Groups** and click "Create target group."
    * Choose a target type (e.g., "Instances"), give it a name, and specify the **protocol** (like HTTP) and **port** (like 80) that your application runs on.
    * Configure the **health checks**, which the load balancer uses to see if an instance is healthy before sending traffic to it.

2.  **Create the Load Balancer:**
    * Go to **Load Balancers** in the EC2 console and click "Create Load Balancer."
    * Choose your type. For web traffic, select **Application Load Balancer**.
    * Give it a **name** and choose a **scheme** (usually "Internet-facing").
    * Select your **VPC** and at least two **Availability Zones** (subnets). This is crucial for high availability.
    * Configure or create a **Security Group** that allows traffic on the ports you need (e.g., port 80 for HTTP).

3.  **Configure Listeners and Routing:**
    * A **listener** checks for connection requests from clients.
    * You'll add a listener for the protocol and port you want the *load balancer* to listen on (e.g., **HTTP** on **port 80**).
    * Create a **default rule** for this listener to **"Forward to"** the Target Group you created in Step 1.
    * (Optional) If you're using HTTPS, you'll add a listener for port 443 and select an SSL certificate from AWS Certificate Manager (ACM).

4.  **Register Targets:**
    * Navigate back to your **Target Group**.
    * Select the "Targets" tab and click "Register targets."
    * Choose the EC2 instances you want to add to this group and click "Include as pending below."
    * Once added, the load balancer will start performing health checks on them.

5.  **Test Your Load Balancer:**
    * Go back to the **Load Balancers** page and select your new load balancer.
    * In the "Description" tab, find its **DNS name** (it will look something like `my-lb-1234567890.us-east-1.elb.amazonaws.com`).
    * Paste this DNS name into your browser. If everything is set up correctly, you should see your application.
