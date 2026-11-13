import React from 'react';
import {AbsoluteFill, Series} from 'remotion';
import {Scene} from './Scene';
import type {VideoProps} from './types';

export const ScriptVideo: React.FC<VideoProps> = ({data}) => (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    <Series>
      {data.scenes.map((scene) => (
        <Series.Sequence key={scene.id} durationInFrames={scene.durationInFrames}>
          <Scene scene={scene} />
        </Series.Sequence>
      ))}
    </Series>
  </AbsoluteFill>
);
