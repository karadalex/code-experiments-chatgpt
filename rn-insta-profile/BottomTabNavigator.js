import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { AntDesign, Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';

import ProfileScreen from './ProfileScreen';
import HomeScreen from './HomeScreen';
import SearchScreen from './SearchScreen';

const Tab = createBottomTabNavigator();

const BottomTabNavigator = () => {
  return (
    <Tab.Navigator
      tabBarOptions={{
        activeTintColor: '#000',
        inactiveTintColor: '#8e8e8e',
        showLabel: false,
        style: {
          height: 60,
          backgroundColor: '#fff',
          borderTopWidth: 0,
          elevation: 0,
        },
      }}
    >
      <Tab.Screen
        name="Home"
        component={HomeScreen}
        options={{
          tabBarIcon: ({ focused }) => (
            <AntDesign name="home" size={24} color={focused ? '#000' : '#8e8e8e'} />
          ),
        }}
      />
      <Tab.Screen
        name="Search"
        component={SearchScreen}
        options={{
          tabBarIcon: ({ focused }) => (
            <Ionicons name="search" size={24} color={focused ? '#000' : '#8e8e8e'} />
          ),
        }}
      />
      <Tab.Screen
        name="Add"
        component={() => null}
        options={{
          tabBarIcon: ({ focused }) => (
            <MaterialCommunityIcons name="plus-box" size={32} color="#00a3ff" />
          ),
          tabBarLabel: () => null,
        }}
        listeners={({ navigation }) => ({
          tabPress: (e) => {
            e.preventDefault();
            navigation.navigate('AddPost');
          },
        })}
      />
      <Tab.Screen
        name="Profile"
        component={ProfileScreen}
        options={{
          tabBarIcon: ({ focused }) => (
            <AntDesign name="user" size={24} color={focused ? '#000' : '#8e8e8e'} />
          ),
        }}
      />
    </Tab.Navigator>
  );
};

export default BottomTabNavigator;
