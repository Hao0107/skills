import React from 'react';
import {AbsoluteFill, Audio, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import type {SceneData} from './types';

const FADE = 12; // frames

export const Scene: React.FC<{scene: SceneData}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {durationInFrames, width} = useVideoConfig();

  const opacity = interpolate(
    frame,
    [0, FADE, durationInFrames - FADE, durationInFrames],
    [0, 1, 1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );
  const titleY = interpolate(frame, [0, 20], [30, 0], {extrapolateRight: 'clamp'});
  const base = width / 1920; // scale fonts with resolution

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.background,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 120 * base,
        opacity,
        fontFamily: 'system-ui, sans-serif',
        color: '#fff',
      }}
    >
      {scene.image ? (
        <Img
          src={staticFile(scene.image)}
          style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: 0.35}}
        />
      ) : null}
      {scene.audio ? <Audio src={staticFile(scene.audio)} /> : null}
      {scene.title ? (
        <h1 style={{fontSize: 96 * base, margin: 0, transform: `translateY(${titleY}px)`, textAlign: 'center'}}>
          {scene.title}
        </h1>
      ) : null}
      {scene.text ? (
        <p style={{fontSize: 48 * base, maxWidth: '80%', textAlign: 'center', lineHeight: 1.4}}>{scene.text}</p>
      ) : null}
    </AbsoluteFill>
  );
};
