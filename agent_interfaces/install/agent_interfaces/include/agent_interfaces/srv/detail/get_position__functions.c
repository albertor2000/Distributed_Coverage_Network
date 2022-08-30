// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from agent_interfaces:srv/GetPosition.idl
// generated code does not contain a copyright notice
#include "agent_interfaces/srv/detail/get_position__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool
agent_interfaces__srv__GetPosition_Request__init(agent_interfaces__srv__GetPosition_Request * msg)
{
  if (!msg) {
    return false;
  }
  // id
  return true;
}

void
agent_interfaces__srv__GetPosition_Request__fini(agent_interfaces__srv__GetPosition_Request * msg)
{
  if (!msg) {
    return;
  }
  // id
}

agent_interfaces__srv__GetPosition_Request *
agent_interfaces__srv__GetPosition_Request__create()
{
  agent_interfaces__srv__GetPosition_Request * msg = (agent_interfaces__srv__GetPosition_Request *)malloc(sizeof(agent_interfaces__srv__GetPosition_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(agent_interfaces__srv__GetPosition_Request));
  bool success = agent_interfaces__srv__GetPosition_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
agent_interfaces__srv__GetPosition_Request__destroy(agent_interfaces__srv__GetPosition_Request * msg)
{
  if (msg) {
    agent_interfaces__srv__GetPosition_Request__fini(msg);
  }
  free(msg);
}


bool
agent_interfaces__srv__GetPosition_Request__Sequence__init(agent_interfaces__srv__GetPosition_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  agent_interfaces__srv__GetPosition_Request * data = NULL;
  if (size) {
    data = (agent_interfaces__srv__GetPosition_Request *)calloc(size, sizeof(agent_interfaces__srv__GetPosition_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = agent_interfaces__srv__GetPosition_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        agent_interfaces__srv__GetPosition_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
agent_interfaces__srv__GetPosition_Request__Sequence__fini(agent_interfaces__srv__GetPosition_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      agent_interfaces__srv__GetPosition_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

agent_interfaces__srv__GetPosition_Request__Sequence *
agent_interfaces__srv__GetPosition_Request__Sequence__create(size_t size)
{
  agent_interfaces__srv__GetPosition_Request__Sequence * array = (agent_interfaces__srv__GetPosition_Request__Sequence *)malloc(sizeof(agent_interfaces__srv__GetPosition_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = agent_interfaces__srv__GetPosition_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
agent_interfaces__srv__GetPosition_Request__Sequence__destroy(agent_interfaces__srv__GetPosition_Request__Sequence * array)
{
  if (array) {
    agent_interfaces__srv__GetPosition_Request__Sequence__fini(array);
  }
  free(array);
}


bool
agent_interfaces__srv__GetPosition_Response__init(agent_interfaces__srv__GetPosition_Response * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // y
  // z
  return true;
}

void
agent_interfaces__srv__GetPosition_Response__fini(agent_interfaces__srv__GetPosition_Response * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
  // z
}

agent_interfaces__srv__GetPosition_Response *
agent_interfaces__srv__GetPosition_Response__create()
{
  agent_interfaces__srv__GetPosition_Response * msg = (agent_interfaces__srv__GetPosition_Response *)malloc(sizeof(agent_interfaces__srv__GetPosition_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(agent_interfaces__srv__GetPosition_Response));
  bool success = agent_interfaces__srv__GetPosition_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
agent_interfaces__srv__GetPosition_Response__destroy(agent_interfaces__srv__GetPosition_Response * msg)
{
  if (msg) {
    agent_interfaces__srv__GetPosition_Response__fini(msg);
  }
  free(msg);
}


bool
agent_interfaces__srv__GetPosition_Response__Sequence__init(agent_interfaces__srv__GetPosition_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  agent_interfaces__srv__GetPosition_Response * data = NULL;
  if (size) {
    data = (agent_interfaces__srv__GetPosition_Response *)calloc(size, sizeof(agent_interfaces__srv__GetPosition_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = agent_interfaces__srv__GetPosition_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        agent_interfaces__srv__GetPosition_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
agent_interfaces__srv__GetPosition_Response__Sequence__fini(agent_interfaces__srv__GetPosition_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      agent_interfaces__srv__GetPosition_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

agent_interfaces__srv__GetPosition_Response__Sequence *
agent_interfaces__srv__GetPosition_Response__Sequence__create(size_t size)
{
  agent_interfaces__srv__GetPosition_Response__Sequence * array = (agent_interfaces__srv__GetPosition_Response__Sequence *)malloc(sizeof(agent_interfaces__srv__GetPosition_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = agent_interfaces__srv__GetPosition_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
agent_interfaces__srv__GetPosition_Response__Sequence__destroy(agent_interfaces__srv__GetPosition_Response__Sequence * array)
{
  if (array) {
    agent_interfaces__srv__GetPosition_Response__Sequence__fini(array);
  }
  free(array);
}
