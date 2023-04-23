import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';

const App = () => {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Image
          style={styles.profilePic}
          source={{uri: 'https://via.placeholder.com/150'}}
        />
        <View style={styles.userInfo}>
          <Text style={styles.username}>JohnDoe</Text>
          <Text style={styles.bio}>Software Developer</Text>
          <Text style={styles.location}>San Francisco, CA</Text>
        </View>
      </View>
      <View style={styles.stats}>
        <View style={styles.stat}>
          <Text style={styles.statNumber}>100</Text>
          <Text style={styles.statTitle}>Posts</Text>
        </View>
        <View style={styles.stat}>
          <Text style={styles.statNumber}>1k</Text>
          <Text style={styles.statTitle}>Followers</Text>
        </View>
        <View style={styles.stat}>
          <Text style={styles.statNumber}>1k</Text>
          <Text style={styles.statTitle}>Following</Text>
        </View>
      </View>
      <View style={styles.photos}>
        <Image
          style={styles.photo}
          source={{uri: 'https://via.placeholder.com/300'}}
        />
        <Image
          style={styles.photo}
          source={{uri: 'https://via.placeholder.com/300'}}
        />
        <Image
          style={styles.photo}
          source={{uri: 'https://via.placeholder.com/300'}}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 10,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  profilePic: {
    width: 100,
    height: 100,
    borderRadius: 50,
    marginRight: 10,
  },
  userInfo: {
    flex: 1,
  },
  username: {
    fontWeight: 'bold',
    fontSize: 20,
    marginBottom: 5,
  },
  bio: {
    color: '#aaa',
    marginBottom: 5,
  },
  location: {
    color: '#aaa',
  },
  stats: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  stat: {
    alignItems: 'center',
  },
  statNumber: {
    fontWeight: 'bold',
    fontSize: 18,
  },
  statTitle: {
    color: '#aaa',
  },
  photos: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  photo: {
    width: '32%',
    aspectRatio: 1,
    marginBottom: 10,
  },
});

export default App;
