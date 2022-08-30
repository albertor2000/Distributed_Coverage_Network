// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice

#ifndef AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__STRUCT_H_
#define AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/GetPosition in the package agent_interfaces.
typedef struct agent_interfaces__srv__GetPosition_Request
{
  int64_t id;
} agent_interfaces__srv__GetPosition_Request;

// Struct for a sequence of agent_interfaces__srv__GetPosition_Request.
typedef struct agent_interfaces__srv__GetPosition_Request__Sequence
{
  agent_interfaces__srv__GetPosition_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agent_interfaces__srv__GetPosition_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/GetPosition in the package agent_interfaces.
typedef struct agent_interfaces__srv__GetPosition_Response
{
  double x;
  double y;
  double z;
} agent_interfaces__srv__GetPosition_Response;

// Struct for a sequence of agent_interfaces__srv__GetPosition_Response.
typedef struct agent_interfaces__srv__GetPosition_Response__Sequence
{
  agent_interfaces__srv__GetPosition_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agent_interfaces__srv__GetPosition_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__STRUCT_H_
