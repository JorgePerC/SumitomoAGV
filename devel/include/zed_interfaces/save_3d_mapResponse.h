// Generated by gencpp from file zed_interfaces/save_3d_mapResponse.msg
// DO NOT EDIT!


#ifndef ZED_INTERFACES_MESSAGE_SAVE_3D_MAPRESPONSE_H
#define ZED_INTERFACES_MESSAGE_SAVE_3D_MAPRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace zed_interfaces
{
template <class ContainerAllocator>
struct save_3d_mapResponse_
{
  typedef save_3d_mapResponse_<ContainerAllocator> Type;

  save_3d_mapResponse_()
    : result(false)
    , info()  {
    }
  save_3d_mapResponse_(const ContainerAllocator& _alloc)
    : result(false)
    , info(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _info_type;
  _info_type info;





  typedef boost::shared_ptr< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> const> ConstPtr;

}; // struct save_3d_mapResponse_

typedef ::zed_interfaces::save_3d_mapResponse_<std::allocator<void> > save_3d_mapResponse;

typedef boost::shared_ptr< ::zed_interfaces::save_3d_mapResponse > save_3d_mapResponsePtr;
typedef boost::shared_ptr< ::zed_interfaces::save_3d_mapResponse const> save_3d_mapResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator1> & lhs, const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result &&
    lhs.info == rhs.info;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator1> & lhs, const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace zed_interfaces

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "929b8c0d7b68510a3f501a60258c746e";
  }

  static const char* value(const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x929b8c0d7b68510aULL;
  static const uint64_t static_value2 = 0x3f501a60258c746eULL;
};

template<class ContainerAllocator>
struct DataType< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "zed_interfaces/save_3d_mapResponse";
  }

  static const char* value(const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool result\n"
"string info\n"
;
  }

  static const char* value(const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
      stream.next(m.info);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct save_3d_mapResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::zed_interfaces::save_3d_mapResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
    s << indent << "info: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.info);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ZED_INTERFACES_MESSAGE_SAVE_3D_MAPRESPONSE_H
