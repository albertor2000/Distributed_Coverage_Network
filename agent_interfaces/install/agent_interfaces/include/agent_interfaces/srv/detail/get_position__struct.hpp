// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice

#ifndef AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__STRUCT_HPP_
#define AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__agent_interfaces__srv__GetPosition_Request __attribute__((deprecated))
#else
# define DEPRECATED__agent_interfaces__srv__GetPosition_Request __declspec(deprecated)
#endif

namespace agent_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetPosition_Request_
{
  using Type = GetPosition_Request_<ContainerAllocator>;

  explicit GetPosition_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0ll;
    }
  }

  explicit GetPosition_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0ll;
    }
  }

  // field types and members
  using _id_type =
    int64_t;
  _id_type id;

  // setters for named parameter idiom
  Type & set__id(
    const int64_t & _arg)
  {
    this->id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agent_interfaces::srv::GetPosition_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const agent_interfaces::srv::GetPosition_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agent_interfaces::srv::GetPosition_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agent_interfaces::srv::GetPosition_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agent_interfaces__srv__GetPosition_Request
    std::shared_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agent_interfaces__srv__GetPosition_Request
    std::shared_ptr<agent_interfaces::srv::GetPosition_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetPosition_Request_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetPosition_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetPosition_Request_

// alias to use template instance with default allocator
using GetPosition_Request =
  agent_interfaces::srv::GetPosition_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agent_interfaces


#ifndef _WIN32
# define DEPRECATED__agent_interfaces__srv__GetPosition_Response __attribute__((deprecated))
#else
# define DEPRECATED__agent_interfaces__srv__GetPosition_Response __declspec(deprecated)
#endif

namespace agent_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetPosition_Response_
{
  using Type = GetPosition_Response_<ContainerAllocator>;

  explicit GetPosition_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0;
      this->z = 0.0;
    }
  }

  explicit GetPosition_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0;
      this->z = 0.0;
    }
  }

  // field types and members
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;
  using _z_type =
    double;
  _z_type z;

  // setters for named parameter idiom
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const double & _arg)
  {
    this->z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agent_interfaces::srv::GetPosition_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const agent_interfaces::srv::GetPosition_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agent_interfaces::srv::GetPosition_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agent_interfaces::srv::GetPosition_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agent_interfaces__srv__GetPosition_Response
    std::shared_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agent_interfaces__srv__GetPosition_Response
    std::shared_ptr<agent_interfaces::srv::GetPosition_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetPosition_Response_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetPosition_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetPosition_Response_

// alias to use template instance with default allocator
using GetPosition_Response =
  agent_interfaces::srv::GetPosition_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agent_interfaces

namespace agent_interfaces
{

namespace srv
{

struct GetPosition
{
  using Request = agent_interfaces::srv::GetPosition_Request;
  using Response = agent_interfaces::srv::GetPosition_Response;
};

}  // namespace srv

}  // namespace agent_interfaces

#endif  // AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__STRUCT_HPP_
