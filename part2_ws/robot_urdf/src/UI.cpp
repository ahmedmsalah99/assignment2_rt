#include "geometry_msgs/msg/twist.hpp"
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
        runUI();
    }
    void runUI(){
        Twist twist;
        Twist zero_twist;
        std::vector<double> twist_vals{0,0,0};
        std::string robot_twise;
        // initializations
        robot_twise = "";
        
        
    
        // take the twist of the turtle as input
        std::vector<std::string> user_msgs = std::vector<std::string>({"x: ","y: ","yaw: "});
        while(rclcpp::ok()){
            for (int i=0;i<3;i++)
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
            twist.angular.z = twist_vals[2];
            pub->publish(twist);
            sleep(1);
            pub->publish(zero_twist);
        }
    }
    rclcpp::Publisher<Twist>::SharedPtr pub;

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