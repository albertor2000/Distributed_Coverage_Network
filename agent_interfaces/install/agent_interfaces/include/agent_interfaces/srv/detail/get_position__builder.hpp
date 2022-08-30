// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice

#ifndef AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__BUILDER_HPP_
#define AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__BUILDER_HPP_

#include "agent_interfaces/srv/detail/get_position__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace agent_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetPosition_Request_id
{
public:
  Init_GetPosition_Request_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agent_interfaces::srv::GetPosition_Request id(::agent_interfaces::srv::GetPosition_Request::_id_type arg)
  {
    msg_.id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agent_interfaces::srv::GetPosition_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agent_interfaces::srv::GetPosition_Request>()
{
  return agent_interfaces::srv::builder::Init_GetPosition_Request_id();
}

}  // namespace agent_interfaces


namespace agent_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetPosition_Response_z
{
public:
  explicit Init_GetPosition_Response_z(::agent_interfaces::srv::GetPosition_Response & msg)
  : msg_(msg)
  {}
  ::agent_interfaces::srv::GetPosition_Response z(::agent_interfaces::srv::GetPosition_Response::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agent_interfaces::srv::GetPosition_Response msg_;
};

class Init_GetPosition_Response_y
{
public:
  explicit Init_GetPosition_Response_y(::agent_interfaces::srv::GetPosition_Response & msg)
  : msg_(msg)
  {}
  Init_GetPosition_Response_z y(::agent_interfaces::srv::GetPosition_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_GetPosition_Response_z(msg_);
  }

private:
  ::agent_interfaces::srv::GetPosition_Response msg_;
};

class Init_GetPosition_Response_x
{
public:
  Init_GetPosition_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetPosition_Response_y x(::agent_interfaces::srv::GetPosition_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_GetPosition_Response_y(msg_);
  }

private:
  ::agent_interfaces::srv::GetPosition_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agent_interfaces::srv::GetPosition_Response>()
{
  return agent_interfaces::srv::builder::Init_GetPosition_Response_x();
}

}  // namespace agent_interfaces

#endif  // AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__BUILDER_HPP_
