// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice

#ifndef AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__FUNCTIONS_H_
#define AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "agent_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "agent_interfaces/srv/detail/get_position__struct.h"

/// Initialize srv/GetPosition message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * agent_interfaces__srv__GetPosition_Request
 * )) before or use
 * agent_interfaces__srv__GetPosition_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
bool
agent_interfaces__srv__GetPosition_Request__init(agent_interfaces__srv__GetPosition_Request * msg);

/// Finalize srv/GetPosition message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Request__fini(agent_interfaces__srv__GetPosition_Request * msg);

/// Create srv/GetPosition message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * agent_interfaces__srv__GetPosition_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
agent_interfaces__srv__GetPosition_Request *
agent_interfaces__srv__GetPosition_Request__create();

/// Destroy srv/GetPosition message.
/**
 * It calls
 * agent_interfaces__srv__GetPosition_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Request__destroy(agent_interfaces__srv__GetPosition_Request * msg);


/// Initialize array of srv/GetPosition messages.
/**
 * It allocates the memory for the number of elements and calls
 * agent_interfaces__srv__GetPosition_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
bool
agent_interfaces__srv__GetPosition_Request__Sequence__init(agent_interfaces__srv__GetPosition_Request__Sequence * array, size_t size);

/// Finalize array of srv/GetPosition messages.
/**
 * It calls
 * agent_interfaces__srv__GetPosition_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Request__Sequence__fini(agent_interfaces__srv__GetPosition_Request__Sequence * array);

/// Create array of srv/GetPosition messages.
/**
 * It allocates the memory for the array and calls
 * agent_interfaces__srv__GetPosition_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
agent_interfaces__srv__GetPosition_Request__Sequence *
agent_interfaces__srv__GetPosition_Request__Sequence__create(size_t size);

/// Destroy array of srv/GetPosition messages.
/**
 * It calls
 * agent_interfaces__srv__GetPosition_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Request__Sequence__destroy(agent_interfaces__srv__GetPosition_Request__Sequence * array);

/// Initialize srv/GetPosition message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * agent_interfaces__srv__GetPosition_Response
 * )) before or use
 * agent_interfaces__srv__GetPosition_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
bool
agent_interfaces__srv__GetPosition_Response__init(agent_interfaces__srv__GetPosition_Response * msg);

/// Finalize srv/GetPosition message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Response__fini(agent_interfaces__srv__GetPosition_Response * msg);

/// Create srv/GetPosition message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * agent_interfaces__srv__GetPosition_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
agent_interfaces__srv__GetPosition_Response *
agent_interfaces__srv__GetPosition_Response__create();

/// Destroy srv/GetPosition message.
/**
 * It calls
 * agent_interfaces__srv__GetPosition_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Response__destroy(agent_interfaces__srv__GetPosition_Response * msg);


/// Initialize array of srv/GetPosition messages.
/**
 * It allocates the memory for the number of elements and calls
 * agent_interfaces__srv__GetPosition_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
bool
agent_interfaces__srv__GetPosition_Response__Sequence__init(agent_interfaces__srv__GetPosition_Response__Sequence * array, size_t size);

/// Finalize array of srv/GetPosition messages.
/**
 * It calls
 * agent_interfaces__srv__GetPosition_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Response__Sequence__fini(agent_interfaces__srv__GetPosition_Response__Sequence * array);

/// Create array of srv/GetPosition messages.
/**
 * It allocates the memory for the array and calls
 * agent_interfaces__srv__GetPosition_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
agent_interfaces__srv__GetPosition_Response__Sequence *
agent_interfaces__srv__GetPosition_Response__Sequence__create(size_t size);

/// Destroy array of srv/GetPosition messages.
/**
 * It calls
 * agent_interfaces__srv__GetPosition_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_agent_interfaces
void
agent_interfaces__srv__GetPosition_Response__Sequence__destroy(agent_interfaces__srv__GetPosition_Response__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // AGENT_INTERFACES__SRV__DETAIL__GET_POSITION__FUNCTIONS_H_
