#include "geometry_msgs/msg/twist.hpp"
#include "geometry_msgs/msg/pose.hpp"
#include "rclcpp/rclcpp.hpp"
#include <string>
#include "unistd.h"
#include<iostream>




using Twist = geometry_msgs::msg::Twist;
class UiNode : public rclcpp::Node
{
    public:
    UiNode():Node("UI")
    {
        pub = this->create_publisher<Twist>("cmd_vel",10);

        feet_pos = this->create_publisher<geometry_msgs::msg::Pose>("feet_pos",10);
        pose_sub = this->create_subscription<std_msgs::msg::String>(
      "/pose", 10, std::bind(&UiNode::pose_callback, this, _1));

      service =this->create_service<example_interfaces::srv::Stop>("stop_robot", &UiNode::stop_robot);
    
        runUI();
    }
    void stop_robot(const std::shared_ptr<example_interfaces::srv::Stop::Request> request,
          std::shared_ptr<example_interfaces::srv::Stop::Response>      response){
            Twist zero_twist;
            pub->publish(zero_twist);
            response->result = true;
    }
    void pose_callback(const geometry_msgs::msg::Pose::SharedPtr msg) const{
        geometry_msgs::msg::Pose pose;
        pose.x = msg->x*3.28;
        pose.y = msg->y*3.28;
        feet_pos->publish(pose);
    }
    void runUI(){
        Twist twist;
        Twist zero_twist;
        std::vector<double> twist_vals{0,0};
        std::string robot_twise;
        // initializations
        robot_twise = "";
        
        
    
        // take the twist of the turtle as input
        std::vector<std::string> user_msgs = std::vector<std::string>({"x: ","y: "});
        while(rclcpp::ok()){
            for (int i=0;i<2;i++)
            {
                while(!is_number(robot_twise))
                {
                    std::cout << user_msgs[i] << std::endl;
                    std::cin >> robot_twise;
                }
                twist_vals[i] = stod(robot_twise);
                robot_twise = "";

            }
            // assign the twist
            twist.linear.x = twist_vals[0];
            twist.linear.y = twist_vals[1];
            // twist.angular.z = twist_vals[2];
            pub->publish(twist);
            // sleep(1);
            rclcpp::sleep_for(std::chrono::milliseconds(1000));
            pub->publish(zero_twist);
        }
    }
    rclcpp::Publisher<Twist>::SharedPtr pub;
    rclcpp::Publisher<geometry_msgs::msg::Pose>::SharedPtr feet_pos;
    rclcpp::Service<example_interfaces::srv::Stop>::SharedPtr service;
    private:
        bool is_number(const std::string& s)
        {
            char* endl = nullptr;
            double val = strtod(s.c_str(), &endl);
            return endl != s.c_str() && *endl == '\0' && val != HUGE_VAL;
        }
};














int main (int argc, char **argv)
{
	// Initialize the node, setup the NodeHandle for handling the communication with the ROS //system  
	rclcpp::init(argc,argv);  

    rclcpp::Rate loop_rate(100);
    
    
    // make UI work

    // while (rclcpp::ok()) {
    //     UI();
    //     // Handle any callbacks (if needed)
    //     rclcpp::spin_some(node);
    //     // Sleep for the remainder of the loop time to maintain the fixed interval
    //     loop_rate.sleep();
    // }

    rclcpp::spin(std::make_shared<UiNode>());
    rclcpp::shutdown();
    return 0;
}