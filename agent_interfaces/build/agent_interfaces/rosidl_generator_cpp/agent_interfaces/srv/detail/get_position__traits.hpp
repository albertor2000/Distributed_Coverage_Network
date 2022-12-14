// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice

#ifndef AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__TRAITS_HPP_
#define AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__TRAITS_HPP_

#include "agent_interfaces/srv/detail/get_position__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<agent_interfaces::srv::GetPosition_Request>()
{
  return "agent_interfaces::srv::GetPosition_Request";
}

template<>
inline const char * name<agent_interfaces::srv::GetPosition_Request>()
{
  return "agent_interfaces/srv/GetPosition_Request";
}

template<>
struct has_fixed_size<agent_interfaces::srv::GetPosition_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<agent_interfaces::srv::GetPosition_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<agent_interfaces::srv::GetPosition_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<agent_interfaces::srv::GetPosition_Response>()
{
  return "agent_interfaces::srv::GetPosition_Response";
}

template<>
inline const char * name<agent_interfaces::srv::GetPosition_Response>()
{
  return "agent_interfaces/srv/GetPosition_Response";
}

template<>
struct has_fixed_size<agent_interfaces::srv::GetPosition_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<agent_interfaces::srv::GetPosition_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<agent_interfaces::srv::GetPosition_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<agent_interfaces::srv::GetPosition>()
{
  return "agent_interfaces::srv::GetPosition";
}

template<>
inline const char * name<agent_interfaces::srv::GetPosition>()
{
  return "agent_interfaces/srv/GetPosition";
}

template<>
struct has_fixed_size<agent_interfaces::srv::GetPosition>
  : std::integral_constant<
    bool,
    has_fixed_size<agent_interfaces::srv::GetPosition_Request>::value &&
    has_fixed_size<agent_interfaces::srv::GetPosition_Response>::value
  >
{
};

template<>
struct has_bounded_size<agent_interfaces::srv::GetPosition>
  : std::integral_constant<
    bool,
    has_bounded_size<agent_interfaces::srv::GetPosition_Request>::value &&
    has_bounded_size<agent_interfaces::srv::GetPosition_Response>::value
  >
{
};

template<>
struct is_service<agent_interfaces::srv::GetPosition>
  : std::true_type
{
};

template<>
struct is_service_request<agent_interfaces::srv::GetPosition_Request>
  : std::true_type
{
};

template<>
struct is_service_response<agent_interfaces::srv::GetPosition_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__TRAITS_HPP_
