import React, { useState } from 'react';

function LikeButton() {
  const [likesCount, setLikesCount] = useState(0);

  const handleLikeClick = () => {
    setLikesCount(likesCount + 1);
  };

  return (
    <button onClick={handleLikeClick}>
      {likesCount} likes
    </button>
  );
}

export default LikeButton;