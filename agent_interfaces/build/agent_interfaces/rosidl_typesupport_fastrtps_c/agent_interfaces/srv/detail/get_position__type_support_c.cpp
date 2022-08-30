// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice
#include "agent_interfaces/srv/detail/get_position__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "agent_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "agent_interfaces/srv/detail/get_position__struct.h"
#include "agent_interfaces/srv/detail/get_position__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _GetPosition_Request__ros_msg_type = agent_interfaces__srv__GetPosition_Request;

static bool _GetPosition_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetPosition_Request__ros_msg_type * ros_message = static_cast<const _GetPosition_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr << ros_message->id;
  }

  return true;
}

static bool _GetPosition_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetPosition_Request__ros_msg_type * ros_message = static_cast<_GetPosition_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr >> ros_message->id;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_agent_interfaces
size_t get_serialized_size_agent_interfaces__srv__GetPosition_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetPosition_Request__ros_msg_type * ros_message = static_cast<const _GetPosition_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name id
  {
    size_t item_size = sizeof(ros_message->id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _GetPosition_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_agent_interfaces__srv__GetPosition_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_agent_interfaces
size_t max_serialized_size_agent_interfaces__srv__GetPosition_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _GetPosition_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_agent_interfaces__srv__GetPosition_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_GetPosition_Request = {
  "agent_interfaces::srv",
  "GetPosition_Request",
  _GetPosition_Request__cdr_serialize,
  _GetPosition_Request__cdr_deserialize,
  _GetPosition_Request__get_serialized_size,
  _GetPosition_Request__max_serialized_size
};

static rosidl_message_type_support_t _GetPosition_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetPosition_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, agent_interfaces, srv, GetPosition_Request)() {
  return &_GetPosition_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "agent_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "agent_interfaces/srv/detail/get_position__struct.h"
// already included above
// #include "agent_interfaces/srv/detail/get_position__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _GetPosition_Response__ros_msg_type = agent_interfaces__srv__GetPosition_Response;

static bool _GetPosition_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetPosition_Response__ros_msg_type * ros_message = static_cast<const _GetPosition_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: x
  {
    cdr << ros_message->x;
  }

  // Field name: y
  {
    cdr << ros_message->y;
  }

  // Field name: z
  {
    cdr << ros_message->z;
  }

  return true;
}

static bool _GetPosition_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetPosition_Response__ros_msg_type * ros_message = static_cast<_GetPosition_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: x
  {
    cdr >> ros_message->x;
  }

  // Field name: y
  {
    cdr >> ros_message->y;
  }

  // Field name: z
  {
    cdr >> ros_message->z;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_agent_interfaces
size_t get_serialized_size_agent_interfaces__srv__GetPosition_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetPosition_Response__ros_msg_type * ros_message = static_cast<const _GetPosition_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name x
  {
    size_t item_size = sizeof(ros_message->x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y
  {
    size_t item_size = sizeof(ros_message->y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name z
  {
    size_t item_size = sizeof(ros_message->z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _GetPosition_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_agent_interfaces__srv__GetPosition_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_agent_interfaces
size_t max_serialized_size_agent_interfaces__srv__GetPosition_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: z
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _GetPosition_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_agent_interfaces__srv__GetPosition_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_GetPosition_Response = {
  "agent_interfaces::srv",
  "GetPosition_Response",
  _GetPosition_Response__cdr_serialize,
  _GetPosition_Response__cdr_deserialize,
  _GetPosition_Response__get_serialized_size,
  _GetPosition_Response__max_serialized_size
};

static rosidl_message_type_support_t _GetPosition_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetPosition_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, agent_interfaces, srv, GetPosition_Response)() {
  return &_GetPosition_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "agent_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "agent_interfaces/srv/get_position.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t GetPosition__callbacks = {
  "agent_interfaces::srv",
  "GetPosition",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, agent_interfaces, srv, GetPosition_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, agent_interfaces, srv, GetPosition_Response)(),
};

static rosidl_service_type_support_t GetPosition__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &GetPosition__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, agent_interfaces, srv, GetPosition)() {
  return &GetPosition__handle;
}

#if defined(__cplusplus)
}
#endif
